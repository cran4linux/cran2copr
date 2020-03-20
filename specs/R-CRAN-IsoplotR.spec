%global packname  IsoplotR
%global packver   3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3
Release:          1%{?dist}
Summary:          Statistical Toolbox for Radiometric Geochronology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
Requires:         R-MASS 
Requires:         R-grDevices 

%description
Plots U-Pb data on Wetherill and Tera-Wasserburg concordia diagrams.
Calculates concordia and discordia ages. Performs linear regression of
measurements with correlated errors using 'York', 'Titterington' and
'Ludwig' approaches. Generates Kernel Density Estimates (KDEs) and
Cumulative Age Distributions (CADs). Produces Multidimensional Scaling
(MDS) configurations and Shepard plots of multi-sample detrital datasets
using the Kolmogorov-Smirnov distance as a dissimilarity measure.
Calculates 40Ar/39Ar ages, isochrons, and age spectra. Computes weighted
means accounting for overdispersion. Calculates U-Th-He (single grain and
central) ages, logratio plots and ternary diagrams. Processes fission
track data using the external detector method and LA-ICP-MS, calculates
central ages and plots fission track and other data on radial (a.k.a.
'Galbraith') plots. Constructs total Pb-U, Pb-Pb, Th-Pb, K-Ca, Re-Os,
Sm-Nd, Lu-Hf, Rb-Sr and 230Th-U isochrons as well as 230Th-U evolution
plots.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/ArAr1.csv
%doc %{rlibdir}/%{packname}/ArAr2.csv
%doc %{rlibdir}/%{packname}/ArAr3.csv
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/constants.json
%doc %{rlibdir}/%{packname}/diseq.csv
%doc %{rlibdir}/%{packname}/DZ.csv
%doc %{rlibdir}/%{packname}/FT1.csv
%doc %{rlibdir}/%{packname}/FT2.csv
%doc %{rlibdir}/%{packname}/FT3.csv
%doc %{rlibdir}/%{packname}/KCa1.csv
%doc %{rlibdir}/%{packname}/KCa2.csv
%doc %{rlibdir}/%{packname}/KCa3.csv
%doc %{rlibdir}/%{packname}/LudwigKDE.csv
%doc %{rlibdir}/%{packname}/LudwigMean.csv
%doc %{rlibdir}/%{packname}/LudwigMixture.csv
%doc %{rlibdir}/%{packname}/LudwigSpectrum.csv
%doc %{rlibdir}/%{packname}/LuHf1.csv
%doc %{rlibdir}/%{packname}/LuHf2.csv
%doc %{rlibdir}/%{packname}/LuHf3.csv
%doc %{rlibdir}/%{packname}/PbPb1.csv
%doc %{rlibdir}/%{packname}/PbPb2.csv
%doc %{rlibdir}/%{packname}/PbPb3.csv
%doc %{rlibdir}/%{packname}/RbSr1.csv
%doc %{rlibdir}/%{packname}/RbSr2.csv
%doc %{rlibdir}/%{packname}/RbSr3.csv
%doc %{rlibdir}/%{packname}/ReOs1.csv
%doc %{rlibdir}/%{packname}/ReOs2.csv
%doc %{rlibdir}/%{packname}/ReOs3.csv
%doc %{rlibdir}/%{packname}/SmNd1.csv
%doc %{rlibdir}/%{packname}/SmNd2.csv
%doc %{rlibdir}/%{packname}/SmNd3.csv
%doc %{rlibdir}/%{packname}/ThPb1.csv
%doc %{rlibdir}/%{packname}/ThPb2.csv
%doc %{rlibdir}/%{packname}/ThPb3.csv
%doc %{rlibdir}/%{packname}/ThU1.csv
%doc %{rlibdir}/%{packname}/ThU2.csv
%doc %{rlibdir}/%{packname}/ThU3.csv
%doc %{rlibdir}/%{packname}/ThU4.csv
%doc %{rlibdir}/%{packname}/UPb1.csv
%doc %{rlibdir}/%{packname}/UPb2.csv
%doc %{rlibdir}/%{packname}/UPb3.csv
%doc %{rlibdir}/%{packname}/UPb4.csv
%doc %{rlibdir}/%{packname}/UPb41.csv
%doc %{rlibdir}/%{packname}/UPb5.csv
%doc %{rlibdir}/%{packname}/UPb6.csv
%doc %{rlibdir}/%{packname}/UPb7.csv
%doc %{rlibdir}/%{packname}/UTh1.csv
%doc %{rlibdir}/%{packname}/UTh2.csv
%doc %{rlibdir}/%{packname}/UThHe.csv
%doc %{rlibdir}/%{packname}/UThSmHe.csv
%{rlibdir}/%{packname}/INDEX
