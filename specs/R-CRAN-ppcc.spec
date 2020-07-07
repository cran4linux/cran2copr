%global packname  ppcc
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Probability Plot Correlation Coefficient Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
Calculates the Probability Plot Correlation Coefficient (PPCC) between a
continuous variable X and a specified distribution. The corresponding
composite hypothesis test that was first introduced by Filliben (1975)
<doi: 10.1080/00401706.1975.10489279> can be performed to test whether the
sample X is element of either the Normal, log-Normal, Exponential,
Uniform, Cauchy, Logistic, Generalized Logistic, Gumbel (GEVI), Weibull,
Generalized Extreme Value, Pearson III (Gamma 2), Mielke's Kappa, Rayleigh
or Generalized Logistic Distribution. The PPCC test is performed with a
fast Monte-Carlo simulation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
