%global packname  stagedtrees
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Staged Event Trees

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Creates and fits staged event tree probability models, which are
probabilistic graphical models capable of representing asymmetric
conditional independence statements for categorical variables. Includes
functions to create, plot and fit staged event trees from data, as well as
many efficient structure learning algorithms. References: Collazo R. A.,
Görgen C. and Smith J. Q. (2018, ISBN:9781498729604). Görgen C., Bigatti
A., Riccomagno E. and Smith J. Q. (2018) <arXiv:1705.09457>. Thwaites P.
A., Smith, J. Q. (2017) <arXiv:1510.00186>. Barclay L. M., Hutton J. L.
and Smith J. Q. (2013) <doi:10.1016/j.ijar.2013.05.006>. Smith J. Q. and
Anderson P. E. (2008) <doi:10.1016/j.artint.2007.05.004>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
