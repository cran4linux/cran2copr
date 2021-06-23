%global __brp_check_rpaths %{nil}
%global packname  GMPro
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Graph Matching with Degree Profiles

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-transport 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-combinat 
Requires:         R-stats 
Requires:         R-CRAN-transport 
Requires:         R-CRAN-igraph 

%description
Functions for graph matching via nodes' degree profiles are provided in
this package. The models we can handle include Erdos-Renyi random graphs
and stochastic block models(SBM). More details are in the reference paper:
Yaofang Hu, Wanjie Wang and Yi Yu (2020) <arXiv:2006.03284>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
