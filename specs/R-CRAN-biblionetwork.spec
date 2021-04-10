%global packname  biblionetwork
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Different Types of Bibliometric Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-data.table 

%description
Functions to find edges for bibliometric networks like bibliographic
coupling network, co-citation network and co-authorship network. The
weights of network edges can be calculated according to different methods,
depending on the type of networks, the type of nodes, and what you want to
analyse. These functions are optimized to be be used on large dataset. The
package contains functions inspired by: Leydesdorff, Loet and Park, Han
Woo (2017) <doi:10.1016/j.joi.2016.11.007>; Perianes-Rodriguez, Antonio,
Ludo Waltman, and Nees Jan Van Eck (2016) <doi:10.1016/j.joi.2016.10.006>;
Sen, Subir K. and Shymal K. Gan (1983)
<http://nopr.niscair.res.in/handle/123456789/28008>; Shen, Si, Zhu,
Danhao, Rousseau, Ronald, Su, Xinning and Wang, Dongbo (2019)
<doi:10.1016/j.joi.2019.01.012>; Zhao, Dangzhi and Strotmann, Andreas
(2008) <doi:10.1002/meet.2008.1450450292>.

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
