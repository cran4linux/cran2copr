%global packname  disttools
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          2%{?dist}
Summary:          Distance Object Manipulation Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides convenient methods for accessing the data in 'dist' objects with
minimal memory and computational overhead. 'disttools' can be used to
extract the distance between any pair or combination of points encoded by
a 'dist' object using only the indices of those points. This is an
improvement over existing functionality, which requires either coercing a
'dist' object into a matrix or calculating the one dimensional index
corresponding to a pair of observations. Coercion to a matrix is
undesirable because doing so doubles the amount of memory required for
storage. In contrast, there is no inherent downside to the latter
solution. However, in part due to several edge cases, correctly and
efficiently implementing such a solution can be challenging. 'disttools'
abstracts away these challenges and provides a simple interface to access
the data in a 'dist' object using the latter approach.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
