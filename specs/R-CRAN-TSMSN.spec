%global __brp_check_rpaths %{nil}
%global packname  TSMSN
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}%{?buildtag}
Summary:          Truncated Scale Mixtures of Skew-Normal Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-progress 

%description
Return the first four moments, estimation of parameters and sample of the
TSMSN distributions (Skew Normal, Skew t, Skew Slash or Skew Contaminated
Normal).

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
