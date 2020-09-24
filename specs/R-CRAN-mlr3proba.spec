%global packname  mlr3proba
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Supervised Learning for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-distr6 >= 1.4.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-mlr3 >= 0.6.0
BuildRequires:    R-CRAN-mlr3misc >= 0.1.7
BuildRequires:    R-CRAN-paradox >= 0.1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-survival 
Requires:         R-CRAN-distr6 >= 1.4.3
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-mlr3 >= 0.6.0
Requires:         R-CRAN-mlr3misc >= 0.1.7
Requires:         R-CRAN-paradox >= 0.1.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-survival 

%description
Provides extensions for probabilistic supervised learning for 'mlr3'.
This includes extending the regression task to probabilistic and interval
regression, adding a survival task, and other specialized models,
predictions, and measures. mlr3extralearners is available from
<https://github.com/mlr-org/mlr3extralearners>.

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
