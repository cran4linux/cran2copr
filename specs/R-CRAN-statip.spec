%global __brp_check_rpaths %{nil}
%global packname  statip
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Functions for Probability Distributions andRegression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-graphics 
BuildRequires:    R-rpart 
BuildRequires:    R-stats 
Requires:         R-CRAN-clue 
Requires:         R-graphics 
Requires:         R-rpart 
Requires:         R-stats 

%description
A collection of miscellaneous statistical functions for probability
distributions: 'dbern()', 'pbern()', 'qbern()', 'rbern()' for the
Bernoulli distribution, and 'distr2name()', 'name2distr()' for
distribution names; probability density estimation: 'densityfun()'; most
frequent value estimation: 'mfv()', 'mfv1()'; other statistical measures
of location: 'cv()' (coefficient of variation), 'midhinge()',
'midrange()', 'trimean()'; construction of histograms: 'histo()',
'find_breaks()'; calculation of the Hellinger distance: 'hellinger()'; use
of classical kernels: 'kernelfun()', 'kernel_properties()'; univariate
piecewise-constant regression: 'picor()'.

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
