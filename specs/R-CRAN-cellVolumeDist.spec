%global __brp_check_rpaths %{nil}
%global packname  cellVolumeDist
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Fit Cell Volume Distributions and Thereby Estimate Cell Growth Rates and Division Times

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm >= 1.1.1
BuildRequires:    R-CRAN-gplots 
Requires:         R-CRAN-minpack.lm >= 1.1.1
Requires:         R-CRAN-gplots 

%description
Implements a methodology for using cell volume distributions to estimate
cell growth rates and division times that is described in the paper
entitled, "Cell Volume Distributions Reveal Cell Growth Rates and Division
Times", by Michael Halter, John T. Elliott, Joseph B. Hubbard, Alessandro
Tona and Anne L. Plant, which is in press in the Journal of Theoretical
Biology.  In order to reproduce the analysis used to obtain Table 1 in the
paper, execute the command "example(fitVolDist)".

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
