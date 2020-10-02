%global packname  shattering
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate the Shattering Coefficient for a Particular Dataset

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-Matrix 
BuildRequires:    R-grDevices 
BuildRequires:    R-base 
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-graphics 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-pdist 
Requires:         R-Matrix 
Requires:         R-grDevices 
Requires:         R-base 
Requires:         R-CRAN-Ryacas 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-pracma 
Requires:         R-graphics 

%description
The Statistical Learning Theory (SLT) provides the theoretical background
to ensure that a supervised algorithm generalizes the mapping f:X -> Y
given f is selected from its search space bias F. This formal result
depends on the Shattering coefficient function N(F,2n) to upper bound the
empirical risk minimization principle, from which one can estimate the
necessary training sample size to ensure the probabilistic learning
convergence and, most importantly, the characterization of the capacity of
F, including its under and overfitting abilities while addressing specific
target problems. In this context, we propose a new approach to estimate
the maximal number of hyperplanes required to shatter a given sample,
i.e., to separate every pair of points from one another, based on the
recent contributions by Har-Peled and Jones in the dataset partitioning
scenario, and use such foundation to analytically compute the Shattering
coefficient function for both binary and multi-class problems. As main
contributions, one can use our approach to study the complexity of the
search space bias F, estimate training sample sizes, and parametrize the
number of hyperplanes a learning algorithm needs to address some
supervised task, what is specially appealing to deep neural networks.
Reference: de Mello, R.F. (2019) "On the Shattering Coefficient of
Supervised Learning Algorithms" <arXiv:1911.05461>; de Mello, R.F., Ponti,
M.A. (2018, ISBN: 978-3319949888) "Machine Learning: A Practical Approach
on the Statistical Learning Theory".

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
