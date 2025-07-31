%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ILSM
%global packver   1.1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Interconnection Structure of Tripartite Interaction Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-plot.matrix 
Requires:         R-stats 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-plot.matrix 

%description
In view of the analysis of the structural characteristics of the
tripartite network has been complete, however, there is still a lack of a
unified operation that can quickly obtain the corresponding
characteristics of the tripartite network. To solve this insufficiency,
'ILSM' was designed for supporting calculating such metrics of tripartite
networks by functions of this R package.

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
