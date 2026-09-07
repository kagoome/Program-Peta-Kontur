import streamlit as st
import os

from src.data_loader import load_excel
from src.interpolation import create_interpolation
from src.contour_map import create_contour_map
from src.visualization_3d import create_3d_surface


st.set_page_config(
    page_title="Sandstone Contour Map",
    page_icon="🗺️",
    layout="wide"
)


st.title("🗺️ Sandstone Contour Map Generator")

st.markdown(
    """
    Aplikasi untuk membuat peta kontur bawah permukaan
    berdasarkan data sumur dari file Excel.
    """
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("⚙️ Pengaturan")

resolution = st.sidebar.slider(
    "Resolusi interpolasi",
    min_value=100,
    max_value=500,
    value=300,
    step=50
)

method = st.sidebar.selectbox(
    "Metode interpolasi",
    [
        "linear",
        "nearest",
        "cubic"
    ]
)

contour_interval = st.sidebar.number_input(
    "Interval kontur",
    min_value=1,
    max_value=1000,
    value=25,
    step=5
)


# =========================================================
# UPLOAD EXCEL
# =========================================================

uploaded_file = st.file_uploader(
    "Upload file Excel",
    type=[
        "xlsx",
        "xls"
    ]
)


if uploaded_file is not None:

    try:

        df = load_excel(
            uploaded_file
        )

        st.success(
            f"Berhasil membaca {len(df)} data sumur."
        )

        # =================================================
        # DATA
        # =================================================

        with st.expander(
            "📋 Lihat data sumur"
        ):

            st.dataframe(
                df,
                use_container_width=True
            )

        # =================================================
        # STATISTIK
        # =================================================

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Jumlah Sumur",
                len(df)
            )

        with col2:
            st.metric(
                "Top Minimum",
                f"{df['Top'].min():.0f}"
            )

        with col3:
            st.metric(
                "Bottom Minimum",
                f"{df['Bottom'].min():.0f}"
            )

        with col4:
            st.metric(
                "Thickness Rata-rata",
                f"{df['Thickness'].mean():.1f}"
            )

        # =================================================
        # INTERPOLASI TOP
        # =================================================

        grid_x_top, grid_y_top, grid_top = (
            create_interpolation(
                df["X"],
                df["Y"],
                df["Top"],
                resolution=resolution,
                method=method
            )
        )

        # =================================================
        # INTERPOLASI BOTTOM
        # =================================================

        grid_x_bottom, grid_y_bottom, grid_bottom = (
            create_interpolation(
                df["X"],
                df["Y"],
                df["Bottom"],
                resolution=resolution,
                method=method
            )
        )

        # =================================================
        # TOP MAP
        # =================================================

        st.header(
            "1. Top Sandstone Map"
        )

        top_fig = create_contour_map(
            grid_x_top,
            grid_y_top,
            grid_top,
            df,
            "Top",
            "TOP OF SANDSTONE",
            contour_interval=contour_interval
        )

        st.pyplot(
            top_fig,
            use_container_width=True
        )

        # =================================================
        # SAVE TOP
        # =================================================

        top_path = "top_sandstone.png"

        top_fig.savefig(
            top_path,
            dpi=100
        )

        with open(
            top_path,
            "rb"
        ) as file:

            st.download_button(
                label="⬇️ Download Top Map",
                data=file,
                file_name="top_sandstone.png",
                mime="image/png"
            )

        # =================================================
        # BOTTOM MAP
        # =================================================

        st.header(
            "2. Bottom Sandstone Map"
        )

        bottom_fig = create_contour_map(
            grid_x_bottom,
            grid_y_bottom,
            grid_bottom,
            df,
            "Bottom",
            "BOTTOM OF SANDSTONE",
            contour_interval=contour_interval
        )

        st.pyplot(
            bottom_fig,
            use_container_width=True
        )

        # =================================================
        # SAVE BOTTOM
        # =================================================

        bottom_path = "bottom_sandstone.png"

        bottom_fig.savefig(
            bottom_path,
            dpi=100
        )

        with open(
            bottom_path,
            "rb"
        ) as file:

            st.download_button(
                label="⬇️ Download Bottom Map",
                data=file,
                file_name="bottom_sandstone.png",
                mime="image/png"
            )

        # =================================================
        # 3D
        # =================================================

        st.header(
            "3. 3D Sandstone Surface"
        )

        fig_3d = create_3d_surface(
            grid_x_top,
            grid_y_top,
            grid_top,
            grid_x_bottom,
            grid_y_bottom,
            grid_bottom,
            df
        )

        st.plotly_chart(
            fig_3d,
            use_container_width=True
        )

        # =================================================
        # THICKNESS
        # =================================================

        st.header(
            "4. Sandstone Thickness"
        )

        st.dataframe(
            df[
                [
                    "No Sumur",
                    "X",
                    "Y",
                    "Top",
                    "Bottom",
                    "Thickness"
                ]
            ],
            use_container_width=True
        )

    except Exception as error:

        st.error(
            f"Terjadi kesalahan: {error}"
        )


else:

    st.info(
        "Silakan upload file Excel untuk memulai."
    )

    st.markdown(
        """
        ### Format Excel

        File Excel harus memiliki kolom:

        - `No Sumur`
        - `Koordinat`
        - `Top`
        - `Bottom`

        Contoh:

        | No Sumur | Koordinat | Top | Bottom |
        |---|---|---:|---:|
        | 1 | 396, 778 | -4400 | -4510 |
        | 2 | 1318, 584 | -4395 | -4490 |
        | 3 | 1911, 340 | -4400 | -4520 |
        """
    )