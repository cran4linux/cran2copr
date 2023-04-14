%global __brp_check_rpaths %{nil}
%global packname  MultiKink
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation and Inference for Multi-Kink Quantile Regression

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-MASS 
Requires:         R-CRAN-quantreg 
Requires:         R-MASS 

%description
Estimation and inference for multiple kink quantile regression. A
bootstrap restarting iterative segmented quantile algorithm is proposed to
estimate the multiple kink quantile regression model conditional on a
given number of change points. The number of kinks is also allowed to be
unknown. In such case, the backward elimination algorithm and the
bootstrap restarting iterative segmented quantile algorithm are combined
to select the number of change points based on a quantile BIC. A
score-type based test statistic is also developed for testing the
existence of kink effect. The package is based on the paper, "Wei Zhong,
Chuang Wan and Wenyang Zhang (2020). Estimation and inference for
multi-kink quantile regression, submitted".

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
