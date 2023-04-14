%global __brp_check_rpaths %{nil}
%global packname  ggmr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Gauss Markov Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-stats >= 3.4.0
Requires:         R-MASS >= 7.3
Requires:         R-stats >= 3.4.0

%description
Implements the generalized Gauss Markov regression, this is useful when
both predictor and response have uncertainty attached to them and also
when covariance within the predictor, within the response and between the
predictor and the response is present. Base on the results published in
guide ISO/TS 28037 (2010) <https://www.iso.org/standard/44473.html>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
