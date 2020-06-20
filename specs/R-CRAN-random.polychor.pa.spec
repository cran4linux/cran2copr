%global packname  random.polychor.pa
%global packver   1.1.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4.3
Release:          1%{?dist}
Summary:          A Parallel Analysis with Polychoric Correlation Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-nFactors 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sfsmisc 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-nFactors 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sfsmisc 

%description
The Function performs a parallel analysis using simulated polychoric
correlation matrices. The nth-percentile of the eigenvalues distribution
obtained from both the randomly generated and the real data polychoric
correlation matrices is returned. A plot comparing the two types of
eigenvalues (real and simulated) will help determine the number of real
eigenvalues that outperform random data. The function is based on the idea
that if real data are non-normal and the polychoric correlation matrix is
needed to perform a Factor Analysis, then the Parallel Analysis method
used to choose a non-random number of factors should also be based on
randomly generated polychoric correlation matrices and not on Pearson
correlation matrices. Random data sets are simulated assuming or a uniform
or a multinomial distribution or via the bootstrap method of resampling
(i.e., random permutations of cases). Also Multigroup Parallel analysis is
made available for random (uniform and multinomial distribution and with
or without difficulty factor) and bootstrap methods. An option to choose
between default or full output is also available as well as a parameter to
print Fit Statistics (Chi-squared, TLI, RMSEA, RMR and BIC) for the factor
solutions indicated by the Parallel Analysis.

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

%files
%{rlibdir}/%{packname}
