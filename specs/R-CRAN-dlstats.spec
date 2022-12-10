%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dlstats
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Download Stats of R Packages

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 
Requires:         R-utils 

%description
Monthly download stats of 'CRAN' and 'Bioconductor' packages. Download
stats of 'CRAN' packages is from the 'RStudio' 'CRAN mirror', see
<https://cranlogs.r-pkg.org:443>. 'Bioconductor' package download stats is
at <https://bioconductor.org/packages/stats/>.

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
