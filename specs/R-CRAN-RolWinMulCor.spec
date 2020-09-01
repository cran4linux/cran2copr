%global packname  RolWinMulCor
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-scales 

%description
Rolling Window Multiple Correlation ('RolWinMulCor') estimates the rolling
(running) window correlation for the bi- and multi-variate cases between
regular (sampled on identical time points) time series, with especial
emphasis to ecological data (although this can be applied to other kinds
of data sets). 'RolWinMulCor' is based on the concept of rolling, running
or sliding window and is useful to evaluate the evolution of correlation
through time and time-scales. 'RolWinMulCor' contains six functions. The
first two focus on the bi-variate case: (1) rolwincor_1win() and (2)
rolwincor_heatmap(), estimate the correlation coefficients and the their
respective p-values for only one window-length (time-scale) and
considering all possible window-lengths or a band of window-lengths,
respectively. The second two functions: (3) rolwinmulcor_1win() and (4)
rolwinmulcor_heatmap() are designed to analyze the multi-variate case,
following the bi-variate case to visually display the results, but these
two approaches are methodologically different: the multi-variate case
estimates the adjusted coefficients of determination instead of the
correlation coefficients. The last two functions: (5) plot_1win() and (6)
plot_heatmap(), are used to represent graphically the outputs of the four
aforementioned functions as simple plots or as heat maps. The functions
contained in 'RolWinMulCor' are highly flexible since this contains
several parameters to control the estimation of correlation and the
features of the plot output, e.g. to remove the (linear) trend contained
in the time series under analysis, to choose different p-value correction
methods (which are used to address the multiple comparison problem) or to
personalise the plot outputs. The 'RolWinMulCor' package also provides
examples with synthetic and real-life ecological time series to exemplify
its use. Methods derived from H. Abdi. (2007)
<https://personal.utdallas.edu/~herve/Abdi-MCC2007-pretty.pdf>, J. M.
Polanco-Martinez (2019) <doi:10.1007/s11071-019-04974-y>, and R. Telford
(2013)
<https://quantpalaeo.wordpress.com/2013/01/04/running-correlations-running-into-problems/>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
