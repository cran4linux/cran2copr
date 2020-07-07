%global packname  clValid
%global packver   0.6-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.8
Release:          2%{?dist}
Summary:          Validation of Clustering Results

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-methods 
BuildRequires:    R-class 
Requires:         R-cluster 
Requires:         R-methods 
Requires:         R-class 

%description
Statistical and biological validation of clustering results. This package
implements Dunn Index, Silhouette, Connectivity, Stability, BHI and BSI.
Further information can be found in Brock, G et al. (2008) <doi:
10.18637/jss.v025.i04>.

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

%files
%{rlibdir}/%{packname}
