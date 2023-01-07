%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BoutrosLab.plotting.general
%global packver   7.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Create Publication-Quality Plots

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-MASS >= 7.3.29
BuildRequires:    R-CRAN-cluster >= 2.0.0
BuildRequires:    R-CRAN-hexbin >= 1.27.0
BuildRequires:    R-CRAN-latticeExtra >= 0.6.27
BuildRequires:    R-CRAN-lattice >= 0.20.35
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-tools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-MASS >= 7.3.29
Requires:         R-CRAN-cluster >= 2.0.0
Requires:         R-CRAN-hexbin >= 1.27.0
Requires:         R-CRAN-latticeExtra >= 0.6.27
Requires:         R-CRAN-lattice >= 0.20.35
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-tools 
Requires:         R-methods 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-e1071 

%description
Contains several plotting functions such as barplots, scatterplots,
heatmaps, as well as functions to combine plots and assist in the creation
of these plots. These functions will give users great ease of use and
customization options in broad use for biomedical applications, as well as
general purpose plotting. Each of the functions also provides valid
default settings to make plotting data more efficient and producing high
quality plots with standard colour schemes simpler. All functions within
this package are capable of producing plots that are of the quality to be
presented in scientific publications and journals. P'ng et al.; BPG:
Seamless, automated and interactive visualization of scientific data; BMC
Bioinformatics 2019 <doi:10.1186/s12859-019-2610-2>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
