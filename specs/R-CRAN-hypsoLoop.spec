%global __brp_check_rpaths %{nil}
%global packname  hypsoLoop
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool Used to Conduct Hypsometric Analysis of a Watershed

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PolynomF 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sjPlot 
Requires:         R-CRAN-PolynomF 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sjPlot 

%description
Functions for generating tables required for drawing and calculating
hypsometric curves and hypsometric integrals. These functions accept as
input the DEM of the region of interest (your watershed) and a spatial
data frame file specifying delineation of sub-catchments within the
watershed. They then generate output in the form of PNG images and HTML
files contained in a folder named "HYPSO_OUTPUT" created in the current
directory. S. K. Sharma, S. Gajbhiye, et al. (2018)
<doi:10.1007/978-981-10-5801-1_19>. Omvir Singh, A. Sarangi, and Milap C.
Sharma (2006) <doi:10.1007/s11269-008-9242-z>. James A. Vanderwaal and
Herbert Ssegane (2013) <doi:10.1111/jawr.12089>.

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
