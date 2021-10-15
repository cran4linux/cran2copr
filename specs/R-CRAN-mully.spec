%global __brp_check_rpaths %{nil}
%global packname  mully
%global packver   2.1.34
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.34
Release:          1%{?dist}%{?buildtag}
Summary:          Create, Modify and Visualize Multi-Layered Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-randomcoloR 
BuildRequires:    R-CRAN-shape 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-randomcoloR 
Requires:         R-CRAN-shape 

%description
Allows the user to create graph with multiple layers. The user can also
modify the layers, the nodes, and the edges. The graph can also be
visualized. Zaynab Hammoud and Frank Kramer (2018)
<doi:10.3390/genes9110519>. More about multilayered graphs and their usage
can be found in our review paper: Zaynab Hammoud and Frank Kramer (2020)
<doi:10.1186/s41044-020-00046-0>.

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
