%global packname  hmm.discnp
%global packver   2.1-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.12
Release:          1%{?dist}
Summary:          Hidden Markov Models with Discrete Non-Parametric ObservationDistributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-nnet >= 7.3.12
Requires:         R-nnet >= 7.3.12

%description
Fits hidden Markov models with discrete non-parametric observation
distributions to data sets.  The observations may be univariate or
bivariate. Simulates data from such models. Finds most probable underlying
hidden states, the most probable sequences of such states, and the log
likelihood of a collection of observations given the parameters of the
model.  Auxiliary predictors are accommodated in the univariate setting.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/inst.c.save
%doc %{rlibdir}/%{packname}/Ratfor
%doc %{rlibdir}/%{packname}/READ_ME
%doc %{rlibdir}/%{packname}/Save
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
