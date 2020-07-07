%global packname  Semblance
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          A Data-Driven Similarity Kernel on Probability Spaces

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 9.6
BuildRequires:    R-CRAN-PerformanceAnalytics >= 1.5.2
BuildRequires:    R-CRAN-msos >= 1.1.0
BuildRequires:    R-CRAN-DescTools >= 0.99.26
Requires:         R-CRAN-fields >= 9.6
Requires:         R-CRAN-PerformanceAnalytics >= 1.5.2
Requires:         R-CRAN-msos >= 1.1.0
Requires:         R-CRAN-DescTools >= 0.99.26

%description
We present a rank-based Mercer kernel to compute a pair-wise similarity
metric corresponding to informative representation of data. We tailor the
development of a kernel to encode our prior knowledge about the data
distribution over a probability space. The philosophical concept behind
our construction is that objects whose feature values fall on the extreme
of that feature’s probability mass distribution are more similar to each
other, than objects whose feature values lie closer to the mean. Semblance
emphasizes features whose values lie far away from the mean of their
probability distribution. The kernel relies on properties empirically
determined from the data and does not assume an underlying distribution.
The use of feature ranks on a probability space ensures that Semblance is
computational efficacious, robust to outliers, and statistically stable,
thus making it widely applicable algorithm for pattern analysis. The
output from the kernel is a square, symmetric matrix that gives proximity
values between pairs of observations.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
