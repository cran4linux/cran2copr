%global __brp_check_rpaths %{nil}
%global packname  stepPlr
%global packver   0.93
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.93
Release:          3%{?dist}%{?buildtag}
Summary:          L2 Penalized Logistic Regression with Stepwise VariableSelection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0

%description
L2 penalized logistic regression for both continuous and discrete
predictors, with forward stagewise/forward stepwise variable selection
procedure.

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
