%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggvolcano
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Publication-Ready Volcano Plots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.1.1
BuildRequires:    R-CRAN-golem >= 0.4.1
BuildRequires:    R-CRAN-config >= 0.3.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-shiny >= 1.8.1.1
Requires:         R-CRAN-golem >= 0.4.1
Requires:         R-CRAN-config >= 0.3.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 

%description
Provides publication-ready volcano plots for visualizing differential
expression results, commonly used in RNA-seq and similar analyses. This
tool helps create high-quality visual representations of data using the
'ggplot2' framework Wickham (2016) <doi:10.1007/978-3-319-24277-4>.

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
