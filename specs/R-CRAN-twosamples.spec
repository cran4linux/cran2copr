%global packname  twosamples
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Permutation Based Two Sample Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
Requires:         R-CRAN-Rcpp >= 0.12.17

%description
Fast randomization based two sample tests. Testing the hypothesis that two
samples come from the same distribution using randomization to create
p-values. Included tests are: Kolmogorov-Smirnov, Kuiper, Cramer-von
Mises, Anderson-Darling, Wasserstein, and DTS. The default test
(two_sample) is based on the DTS test statistic, as it is the most
powerful, and thus most useful to most users. The DTS test statistic
builds on the Wasserstein distance by using a weighting scheme like that
of Anderson-Darling. See the companion paper at <arXiv:2007.01360> or
<https://codowd.com/public/DTS.pdf> for details of that test statistic,
and non-standard uses of the package (parallel for big N, weighted
observations, one sample tests, etc). We also include the permutation
scheme to make test building simple for others.

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
