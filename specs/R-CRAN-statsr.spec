%global packname  statsr
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Companion Package for Statistics with R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-tidyr 

%description
Provides functions and datasets to support inference with the open access
book "An Introduction to Bayesian Thinking", available online
<https://statswithr.github.io/book> and online videos for the "Statistics
with R Specialization"
<https://www.coursera.org/specializations/statistics>. which includes an
introduction to Bayesian inference and decision making for one and two
sample credible intervals and hypothesis testing for Gaussian and Binomial
data, in addition to frequentist inference using model-based and
randomization-based methods. To help with understanding concepts, 'shiny'
applications are used to aide visualization of sampling distributions,
credible intervals, hypothesis testing, Lindley's and Bartlett's
paradoxes. For development versions or to report issues, please visit
<https://github.com/StatsWithR/statsr>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/lab.css
%{rlibdir}/%{packname}/INDEX
