%global __brp_check_rpaths %{nil}
%global packname  hmeasure
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          The H-Measure and Other Scalar Classification PerformanceMetrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Classification performance metrics that are derived from the ROC curve of
a classifier. The package includes the H-measure performance metric as
described in <http://link.springer.com/article/10.1007/s10994-009-5119-5>,
which computes the minimum total misclassification cost, integrating over
any uncertainty about the relative misclassification costs, as per a
user-defined prior. It also offers a one-stop-shop for other scalar
metrics of performance, including sensitivity, specificity and many
others, and also offers plotting tools for ROC curves and related
statistics.

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
