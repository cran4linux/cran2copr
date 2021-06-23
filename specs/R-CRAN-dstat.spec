%global __brp_check_rpaths %{nil}
%global packname  dstat
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Conditional Sensitivity Analysis for Matched ObservationalStudies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
A d-statistic tests the null hypothesis of no treatment effect in a
matched, nonrandomized study of the effects caused by treatments.  A
d-statistic focuses on subsets of matched pairs that demonstrate
insensitivity to unmeasured bias in such an observational study,
correcting for double-use of the data by conditional inference. This
conditional inference can, in favorable circumstances, substantially
increase the power of a sensitivity analysis (Rosenbaum (2010)
<doi:10.1007/978-1-4419-1213-8_14>).  There are two examples, one
concerning unemployment from Lalive et al. (2006)
<doi:10.1111/j.1467-937X.2006.00406.x>, the other concerning smoking and
periodontal disease from Rosenbaum (2017) <doi:10.1214/17-STS621>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
