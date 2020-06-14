%global packname  KSgeneral
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Computing P-Values of the K-S Test for (Dis)Continuous NullDistribution

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.3.4
Requires:         fftw
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-dgof 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-MASS 
Requires:         R-CRAN-dgof 

%description
Computes a p-value of the one-sample two-sided (or one-sided, as a special
case) Kolmogorov-Smirnov (KS) statistic, for any fixed critical level, and
an arbitrary, possibly large sample size for a pre-specified purely
discrete, mixed or continuous cumulative distribution function (cdf) under
the null hypothesis. If a data sample is supplied, 'KSgeneral' computes
the p-value corresponding to the value of the KS test statistic computed
based on the user provided data sample. The package 'KSgeneral' implements
a novel, accurate and efficient method named Exact-KS-FFT, expressing the
p-value as a double-boundary non-crossing probability for a homogeneous
Poisson process, which is then efficiently computed using Fast Fourier
Transform (FFT). The package can also be used to compute and plot the
complementary cdf of the KS statistic which is known to depend on the
hypothesized distribution when the latter is discontinuous (i.e. purely
discrete or mixed).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%license %{rlibdir}/%{packname}/FFTW_LICENSE.TXT
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
