%global packname  RolWinMulCor
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          Subroutines to Estimate Rolling Window Multiple Correlation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-stats 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-colorspace 

%description
Rolling Window Multiple Correlation ('RolWinMulCor') estimates the rolling
(running) window correlation for the bi- and multi-variate cases between
regular (sampled on identical time points) time series, with especial
emphasis to environmental data (although this can be applied to other
kinds of data sets). 'RolWinMulCor' is based on the concept of rolling or
running window and is useful to evaluate the evolution of correlation
through time and time-scales. 'RolWinMulCor' contains four functions: (1)
the first two functions are focus on the bi-variate case, one of them
produces a simple plot of correlation coefficients and p-values (<=0.05)
for only one window-length (time-scale), and the other function produces a
heat map for the statistically significant (p-values <=0.05) correlation
coefficients taking into account all the possible window-lengths (which
are determined by the number of elements of the time series under
analysis) or for a band of window-lengths; (2) the second two functions
are designed to analyse the multi-variate case and follow the bi-variate
case to display visually the results although these two methods are
different. The four functions contained in 'RolWinMulCor' are highly
flexible since this contains a great number of parameters to control the
estimation of correlation and the features of the plot output, e.g. to
remove the (linear) trend contained in the time series under analysis, to
choose different p-value correction methods (which are used to address the
multiple comparison problem) or to personalise the plot output (e.g. this
can be displayed in the screen or can be saved as PNG, JPEG, EPS or PDF
formats). The 'RolWinMulCor' package also provides examples with synthetic
and real environmental time series to exemplify its use. Methods derived
from H. Abdi. (2007)
<https://personal.utdallas.edu/~herve/Abdi-MCC2007-pretty.pdf>, J. M.
Polanco-Martinez (2019) <doi:10.1007/s11071-019-04974-y>, and R. Telford
(2013)
<https://quantpalaeo.wordpress.com/2013/01/04/running-correlations-running-into-problems/>.

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
%{rlibdir}/%{packname}/INDEX
