%global packname  TKF
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          2%{?dist}
Summary:          Pairwise Distance Estimation with TKF91 and TKF92 Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-ape >= 3.2
BuildRequires:    R-CRAN-phangorn >= 1.99.12
BuildRequires:    R-CRAN-phytools >= 0.4.45
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-ape >= 3.2
Requires:         R-CRAN-phangorn >= 1.99.12
Requires:         R-CRAN-phytools >= 0.4.45
Requires:         R-methods 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-numDeriv 

%description
Pairwise evolutionary distance estimation between protein sequences with
the TKF91 and TKF92 model, which consider all the possible paths of
transforming from one sequence to another.

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
