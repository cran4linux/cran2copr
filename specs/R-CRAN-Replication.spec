%global packname  Replication
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Test Replications by Means of the Prior Predictive p-Value

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-runjags >= 2.0.4.2
BuildRequires:    R-CRAN-lavaan >= 0.6.3
BuildRequires:    R-CRAN-blavaan 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-runjags >= 2.0.4.2
Requires:         R-CRAN-lavaan >= 0.6.3
Requires:         R-CRAN-blavaan 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-quadprog 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-rjags 

%description
Allows for the computation of a prior predictive p-value to test
replication of relevant features of original studies. Relevant features
are captured in informative hypotheses. The package also allows for the
computation of power. The statistical underpinnings are described in
Zondervan-Zwijnenburg (2019) <doi:10.31234/osf.io/uvh5s>.

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
