%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deaviz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of Data Envelopment Analysis Problems

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
High-dimensional visualization methods for data envelopment analysis
(DEA), gathering in one place techniques that have appeared in the
literature but remained scattered and largely unimplemented:
cross-efficiency matrix unfolding, the Porembski network with lambda
edges, principal component analysis biplots, multidimensional-scaling
colour-plots, self-organizing maps, the Costa bi-dimensional efficient
frontier, parallel coordinates, radar charts, panel-data trajectory
biplots, peer and reference networks, and a set of descriptive plots. The
package is built around a single validated dea_data() object and uses the
'Benchmarking' package as its DEA engine. The implemented methods draw on
a body of literature; representative references include Doyle and Green
(1994) <doi:10.1057/jors.1994.84>, Porembski, Breitenstein and Alpar
(2005) <doi:10.1007/s11123-005-1328-5> and Bana e Costa, Soares de Mello
and Angulo Meza (2016) <doi:10.1016/j.ejor.2016.05.012>.

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
