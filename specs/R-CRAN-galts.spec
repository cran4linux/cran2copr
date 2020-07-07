%global packname  galts
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}
Summary:          Genetic Algorithms and C-Steps Based LTS (Least Trimmed Squares)Estimation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-genalg 
BuildRequires:    R-CRAN-DEoptim 
Requires:         R-CRAN-genalg 
Requires:         R-CRAN-DEoptim 

%description
Includes the ga.lts() function that estimates LTS (Least Trimmed Squares)
parameters using genetic algorithms and C-steps. ga.lts() constructs a
genetic algorithm to form a basic subset and iterates C-steps as defined
in Rousseeuw and van-Driessen (2006) to calculate the cost value of the
LTS criterion. OLS (Ordinary Least Squares) regression is known to be
sensitive to outliers. A single outlying observation can change the values
of estimated parameters. LTS is a resistant estimator even the number of
outliers is up to half of the data. This package is for estimating the LTS
parameters with lower bias and variance in a reasonable time. Version
>=1.3 includes the function medmad for fast outlier detection in linear
regression.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
