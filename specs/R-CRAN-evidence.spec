%global packname  evidence
%global packver   0.8.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.10
Release:          3%{?dist}
Summary:          Analysis of Scientific Evidence Using Bayesian and LikelihoodMethods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-LearnBayes 
BuildRequires:    R-CRAN-LaplacesDemon 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-rstanarm 
Requires:         R-CRAN-loo 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-LearnBayes 
Requires:         R-CRAN-LaplacesDemon 

%description
Bayesian (and some likelihoodist) functions as alternatives to
hypothesis-testing functions in R base using a user interface patterned
after those of R's hypothesis testing functions. See McElreath (2016,
ISBN: 978-1-4822-5344-3), Gelman and Hill (2007, ISBN: 0-521-68689-X) (new
edition in preparation) and Albert (2009, ISBN: 978-0-387-71384-7) for
good introductions to Bayesian analysis and Pawitan (2002, ISBN:
0-19-850765-8) for the Likelihood approach.  The functions in the package
also make extensive use of graphical displays for data exploration and
model comparison.

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
%{rlibdir}/%{packname}/INDEX
