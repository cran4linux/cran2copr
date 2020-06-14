%global packname  knotR
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Knot Diagrams using Bezier Curves

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Makes nice pictures of knots using Bezier curves and numerical
optimization.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/10_1_worker.R
%doc %{rlibdir}/%{packname}/10_1.svg
%doc %{rlibdir}/%{packname}/10_123.svg
%doc %{rlibdir}/%{packname}/10_47_worker.R
%doc %{rlibdir}/%{packname}/10_47.svg
%doc %{rlibdir}/%{packname}/10_61_worker.R
%doc %{rlibdir}/%{packname}/10_61.svg
%doc %{rlibdir}/%{packname}/10_75_worker.R
%doc %{rlibdir}/%{packname}/10_75.svg
%doc %{rlibdir}/%{packname}/11_9.svg
%doc %{rlibdir}/%{packname}/20-crossings-ornamental-knot.svg
%doc %{rlibdir}/%{packname}/3_1_alternative.svg
%doc %{rlibdir}/%{packname}/3_1_not_symmetric.svg
%doc %{rlibdir}/%{packname}/3_1_worker.R
%doc %{rlibdir}/%{packname}/3_1.svg
%doc %{rlibdir}/%{packname}/3_1a_worker.R
%doc %{rlibdir}/%{packname}/4_1_first_draft.svg
%doc %{rlibdir}/%{packname}/4_1_worker.R
%doc %{rlibdir}/%{packname}/4_1.svg
%doc %{rlibdir}/%{packname}/5_1_worker.R
%doc %{rlibdir}/%{packname}/5_1.svg
%doc %{rlibdir}/%{packname}/5_2_worker.R
%doc %{rlibdir}/%{packname}/5_2.svg
%doc %{rlibdir}/%{packname}/6_1_worker.R
%doc %{rlibdir}/%{packname}/6_1.svg
%doc %{rlibdir}/%{packname}/6_2_worker.R
%doc %{rlibdir}/%{packname}/6_2.svg
%doc %{rlibdir}/%{packname}/6_3_worker.R
%doc %{rlibdir}/%{packname}/6_3.svg
%doc %{rlibdir}/%{packname}/7_1_worker.R
%doc %{rlibdir}/%{packname}/7_1.svg
%doc %{rlibdir}/%{packname}/7_2_worker.R
%doc %{rlibdir}/%{packname}/7_2.svg
%doc %{rlibdir}/%{packname}/7_3_worker.R
%doc %{rlibdir}/%{packname}/7_3.svg
%doc %{rlibdir}/%{packname}/7_4_experimental.svg
%doc %{rlibdir}/%{packname}/7_4_worker.R
%doc %{rlibdir}/%{packname}/7_4.svg
%doc %{rlibdir}/%{packname}/7_4experimentalworker.R
%doc %{rlibdir}/%{packname}/7_5_worker.R
%doc %{rlibdir}/%{packname}/7_5.svg
%doc %{rlibdir}/%{packname}/7_6_first_draft.svg
%doc %{rlibdir}/%{packname}/7_6_worker.R
%doc %{rlibdir}/%{packname}/7_6.svg
%doc %{rlibdir}/%{packname}/7_7_worker.R
%doc %{rlibdir}/%{packname}/7_7.svg
%doc %{rlibdir}/%{packname}/7_7a_worker.R
%doc %{rlibdir}/%{packname}/7_7a.svg
%doc %{rlibdir}/%{packname}/8_1_worker.R
%doc %{rlibdir}/%{packname}/8_1.svg
%doc %{rlibdir}/%{packname}/8_10_worker.R
%doc %{rlibdir}/%{packname}/8_10.svg
%doc %{rlibdir}/%{packname}/8_11_worker.R
%doc %{rlibdir}/%{packname}/8_11.svg
%doc %{rlibdir}/%{packname}/8_12_worker.R
%doc %{rlibdir}/%{packname}/8_12.svg
%doc %{rlibdir}/%{packname}/8_13_worker.R
%doc %{rlibdir}/%{packname}/8_13.svg
%doc %{rlibdir}/%{packname}/8_14_worker.R
%doc %{rlibdir}/%{packname}/8_14.svg
%doc %{rlibdir}/%{packname}/8_15_worker.R
%doc %{rlibdir}/%{packname}/8_15.svg
%doc %{rlibdir}/%{packname}/8_16_worker.R
%doc %{rlibdir}/%{packname}/8_16.svg
%doc %{rlibdir}/%{packname}/8_17_worker.R
%doc %{rlibdir}/%{packname}/8_17.svg
%doc %{rlibdir}/%{packname}/8_18_worker.R
%doc %{rlibdir}/%{packname}/8_18.svg
%doc %{rlibdir}/%{packname}/8_19_alternative_worker.R
%doc %{rlibdir}/%{packname}/8_19_alternative.svg
%doc %{rlibdir}/%{packname}/8_19_worker.R
%doc %{rlibdir}/%{packname}/8_19.svg
%doc %{rlibdir}/%{packname}/8_19a.svg
%doc %{rlibdir}/%{packname}/8_2_worker.R
%doc %{rlibdir}/%{packname}/8_2.svg
%doc %{rlibdir}/%{packname}/8_20_worker.R
%doc %{rlibdir}/%{packname}/8_20.svg
%doc %{rlibdir}/%{packname}/8_21_worker.R
%doc %{rlibdir}/%{packname}/8_21.svg
%doc %{rlibdir}/%{packname}/8_3_worker.R
%doc %{rlibdir}/%{packname}/8_3.svg
%doc %{rlibdir}/%{packname}/8_4_alternative.svg
%doc %{rlibdir}/%{packname}/8_4_worker.R
%doc %{rlibdir}/%{packname}/8_4.svg
%doc %{rlibdir}/%{packname}/8_4a_worker.R
%doc %{rlibdir}/%{packname}/8_5_worker.R
%doc %{rlibdir}/%{packname}/8_5.svg
%doc %{rlibdir}/%{packname}/8_6_worker.R
%doc %{rlibdir}/%{packname}/8_6.svg
%doc %{rlibdir}/%{packname}/8_7_worker.R
%doc %{rlibdir}/%{packname}/8_7.svg
%doc %{rlibdir}/%{packname}/8_8_worker.R
%doc %{rlibdir}/%{packname}/8_8.svg
%doc %{rlibdir}/%{packname}/8_9_worker.R
%doc %{rlibdir}/%{packname}/8_9.svg
%doc %{rlibdir}/%{packname}/9_1_worker.R
%doc %{rlibdir}/%{packname}/9_1.svg
%doc %{rlibdir}/%{packname}/9_10_worker.R
%doc %{rlibdir}/%{packname}/9_10.svg
%doc %{rlibdir}/%{packname}/9_11_worker.R
%doc %{rlibdir}/%{packname}/9_11.svg
%doc %{rlibdir}/%{packname}/9_12_worker.R
%doc %{rlibdir}/%{packname}/9_12.svg
%doc %{rlibdir}/%{packname}/9_13_worker.R
%doc %{rlibdir}/%{packname}/9_13.svg
%doc %{rlibdir}/%{packname}/9_14_worker.R
%doc %{rlibdir}/%{packname}/9_14.svg
%doc %{rlibdir}/%{packname}/9_15_worker.R
%doc %{rlibdir}/%{packname}/9_15.svg
%doc %{rlibdir}/%{packname}/9_16_worker.R
%doc %{rlibdir}/%{packname}/9_16.svg
%doc %{rlibdir}/%{packname}/9_17_worker.R
%doc %{rlibdir}/%{packname}/9_17.svg
%doc %{rlibdir}/%{packname}/9_18_worker.R
%doc %{rlibdir}/%{packname}/9_18.svg
%doc %{rlibdir}/%{packname}/9_19_worker.R
%doc %{rlibdir}/%{packname}/9_19.svg
%doc %{rlibdir}/%{packname}/9_2_worker.R
%doc %{rlibdir}/%{packname}/9_2.svg
%doc %{rlibdir}/%{packname}/9_20_worker.R
%doc %{rlibdir}/%{packname}/9_20.svg
%doc %{rlibdir}/%{packname}/9_21_worker.R
%doc %{rlibdir}/%{packname}/9_21.svg
%doc %{rlibdir}/%{packname}/9_22_worker.R
%doc %{rlibdir}/%{packname}/9_22.svg
%doc %{rlibdir}/%{packname}/9_23_worker.R
%doc %{rlibdir}/%{packname}/9_23.svg
%doc %{rlibdir}/%{packname}/9_24_worker.R
%doc %{rlibdir}/%{packname}/9_24.svg
%doc %{rlibdir}/%{packname}/9_25_worker.R
%doc %{rlibdir}/%{packname}/9_25.svg
%doc %{rlibdir}/%{packname}/9_26_worker.R
%doc %{rlibdir}/%{packname}/9_26.svg
%doc %{rlibdir}/%{packname}/9_27_worker.R
%doc %{rlibdir}/%{packname}/9_27.svg
%doc %{rlibdir}/%{packname}/9_28_worker.R
%doc %{rlibdir}/%{packname}/9_28.svg
%doc %{rlibdir}/%{packname}/9_29_worker.R
%doc %{rlibdir}/%{packname}/9_29.svg
%doc %{rlibdir}/%{packname}/9_3_worker.R
%doc %{rlibdir}/%{packname}/9_3.svg
%doc %{rlibdir}/%{packname}/9_30_worker.R
%doc %{rlibdir}/%{packname}/9_30.svg
%doc %{rlibdir}/%{packname}/9_31_worker.R
%doc %{rlibdir}/%{packname}/9_31.svg
%doc %{rlibdir}/%{packname}/9_32_worker.R
%doc %{rlibdir}/%{packname}/9_32.svg
%doc %{rlibdir}/%{packname}/9_33_worker.R
%doc %{rlibdir}/%{packname}/9_33.svg
%doc %{rlibdir}/%{packname}/9_34_worker.R
%doc %{rlibdir}/%{packname}/9_34.svg
%doc %{rlibdir}/%{packname}/9_35_worker.R
%doc %{rlibdir}/%{packname}/9_35.svg
%doc %{rlibdir}/%{packname}/9_36_worker.R
%doc %{rlibdir}/%{packname}/9_36.svg
%doc %{rlibdir}/%{packname}/9_37_worker.R
%doc %{rlibdir}/%{packname}/9_37.svg
%doc %{rlibdir}/%{packname}/9_38_worker.R
%doc %{rlibdir}/%{packname}/9_38.svg
%doc %{rlibdir}/%{packname}/9_39_worker.R
%doc %{rlibdir}/%{packname}/9_39.svg
%doc %{rlibdir}/%{packname}/9_4_worker.R
%doc %{rlibdir}/%{packname}/9_4.svg
%doc %{rlibdir}/%{packname}/9_40_worker.R
%doc %{rlibdir}/%{packname}/9_40.svg
%doc %{rlibdir}/%{packname}/9_41_worker.R
%doc %{rlibdir}/%{packname}/9_41.svg
%doc %{rlibdir}/%{packname}/9_42_worker.R
%doc %{rlibdir}/%{packname}/9_42.svg
%doc %{rlibdir}/%{packname}/9_43_worker.R
%doc %{rlibdir}/%{packname}/9_43.svg
%doc %{rlibdir}/%{packname}/9_44_worker.R
%doc %{rlibdir}/%{packname}/9_44.svg
%doc %{rlibdir}/%{packname}/9_45_worker.R
%doc %{rlibdir}/%{packname}/9_45.svg
%doc %{rlibdir}/%{packname}/9_46_worker.R
%doc %{rlibdir}/%{packname}/9_46.svg
%doc %{rlibdir}/%{packname}/9_47_worker.R
%doc %{rlibdir}/%{packname}/9_47.svg
%doc %{rlibdir}/%{packname}/9_48_worker.R
%doc %{rlibdir}/%{packname}/9_48.svg
%doc %{rlibdir}/%{packname}/9_49_worker.R
%doc %{rlibdir}/%{packname}/9_49.svg
%doc %{rlibdir}/%{packname}/9_5_worker.R
%doc %{rlibdir}/%{packname}/9_5.svg
%doc %{rlibdir}/%{packname}/9_6_worker.R
%doc %{rlibdir}/%{packname}/9_6.svg
%doc %{rlibdir}/%{packname}/9_7_worker.R
%doc %{rlibdir}/%{packname}/9_7.svg
%doc %{rlibdir}/%{packname}/9_8_worker.R
%doc %{rlibdir}/%{packname}/9_8.svg
%doc %{rlibdir}/%{packname}/9_9_worker.R
%doc %{rlibdir}/%{packname}/9_9.svg
%doc %{rlibdir}/%{packname}/amphichiral15_worker.R
%doc %{rlibdir}/%{packname}/amphichiral15.svg
%doc %{rlibdir}/%{packname}/celtic_worker.R
%doc %{rlibdir}/%{packname}/celtic.svg
%doc %{rlibdir}/%{packname}/celtic2_worker.R
%doc %{rlibdir}/%{packname}/celtic2.svg
%doc %{rlibdir}/%{packname}/celtic3_worker.R
%doc %{rlibdir}/%{packname}/celtic3.svg
%doc %{rlibdir}/%{packname}/D16_worker.R
%doc %{rlibdir}/%{packname}/D16.svg
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fiveloops_worker.R
%doc %{rlibdir}/%{packname}/fiveloops.svg
%doc %{rlibdir}/%{packname}/flower_worker.R
%doc %{rlibdir}/%{packname}/flower.svg
%doc %{rlibdir}/%{packname}/fourloops_worker.R
%doc %{rlibdir}/%{packname}/fourloops.svg
%doc %{rlibdir}/%{packname}/infinity.svg
%doc %{rlibdir}/%{packname}/k11a1_worker.R
%doc %{rlibdir}/%{packname}/k11a1.svg
%doc %{rlibdir}/%{packname}/k11a179_worker.R
%doc %{rlibdir}/%{packname}/k11a179.svg
%doc %{rlibdir}/%{packname}/k11a203_worker.R
%doc %{rlibdir}/%{packname}/k11a203.svg
%doc %{rlibdir}/%{packname}/k11a361_worker.R
%doc %{rlibdir}/%{packname}/k11a361.svg
%doc %{rlibdir}/%{packname}/k11a43_worker.R
%doc %{rlibdir}/%{packname}/k11a43.svg
%doc %{rlibdir}/%{packname}/k11n157_morenodes_worker.R
%doc %{rlibdir}/%{packname}/k11n157_morenodes.svg
%doc %{rlibdir}/%{packname}/k11n157_worker.R
%doc %{rlibdir}/%{packname}/k11n157.svg
%doc %{rlibdir}/%{packname}/k11n22_worker.R
%doc %{rlibdir}/%{packname}/k11n22.svg
%doc %{rlibdir}/%{packname}/k12a_0614_worker.R
%doc %{rlibdir}/%{packname}/k12a_0614.svg
%doc %{rlibdir}/%{packname}/k12n_0242_worker.R
%doc %{rlibdir}/%{packname}/k12n_0242.svg
%doc %{rlibdir}/%{packname}/k12n_0411_worker.R
%doc %{rlibdir}/%{packname}/k12n_0411.svg
%doc %{rlibdir}/%{packname}/k3_1_worker.R
%doc %{rlibdir}/%{packname}/longthin_worker.R
%doc %{rlibdir}/%{packname}/longthin.svg
%doc %{rlibdir}/%{packname}/ochiai_worker.R
%doc %{rlibdir}/%{packname}/ochiai.svg
%doc %{rlibdir}/%{packname}/ornamental_worker.R
%doc %{rlibdir}/%{packname}/ornamental12.svg
%doc %{rlibdir}/%{packname}/ornamental20.svg
%doc %{rlibdir}/%{packname}/perko_A_worker.R
%doc %{rlibdir}/%{packname}/perko_A.svg
%doc %{rlibdir}/%{packname}/perko_B_worker.R
%doc %{rlibdir}/%{packname}/perko_B.svg
%doc %{rlibdir}/%{packname}/perko_worker.R
%doc %{rlibdir}/%{packname}/pretzel_2_3_7.svg
%doc %{rlibdir}/%{packname}/pretzel_237_worker.R
%doc %{rlibdir}/%{packname}/pretzel_35735_worker.R
%doc %{rlibdir}/%{packname}/pretzel_7_3_7.svg
%doc %{rlibdir}/%{packname}/pretzel_737_worker.R
%doc %{rlibdir}/%{packname}/pretzel_p3_p5_p7_m3_m5.svg
%doc %{rlibdir}/%{packname}/product_knot.svg
%doc %{rlibdir}/%{packname}/product_worker.R
%doc %{rlibdir}/%{packname}/reefknot_worker.R
%doc %{rlibdir}/%{packname}/reefknot.svg
%doc %{rlibdir}/%{packname}/s2.R
%doc %{rlibdir}/%{packname}/satellite_worker.R
%doc %{rlibdir}/%{packname}/satellite.svg
%doc %{rlibdir}/%{packname}/stuff.txt
%doc %{rlibdir}/%{packname}/sum_3_1_and_4_1_worker.R
%doc %{rlibdir}/%{packname}/sum_3_1_and_4_1.svg
%doc %{rlibdir}/%{packname}/T20_worker.R
%doc %{rlibdir}/%{packname}/T20.svg
%doc %{rlibdir}/%{packname}/three_figure_eights_worker.R
%doc %{rlibdir}/%{packname}/three_figure_eights.svg
%doc %{rlibdir}/%{packname}/trefoil_of_trefoils_worker.R
%doc %{rlibdir}/%{packname}/trefoil_of_trefoils.svg
%doc %{rlibdir}/%{packname}/trefoil_worker.R
%doc %{rlibdir}/%{packname}/triloop_worker.R
%doc %{rlibdir}/%{packname}/triloop.svg
%doc %{rlibdir}/%{packname}/unknot_worker.R
%doc %{rlibdir}/%{packname}/unknot.svg
%{rlibdir}/%{packname}/INDEX
