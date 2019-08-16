%global packname  bit
%global packver   1.1-14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.14
Release:          1%{?dist}
Summary:          A Class for Vectors of 1-Bit Booleans

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.9.2
Requires:         R-core >= 2.9.2

%description
True boolean datatype (no NAs), coercion from and to logicals, integers
and integer subscripts; fast boolean operators and fast summary
statistics. With 'bit' vectors you can store true binary booleans
{FALSE,TRUE} at the expense of 1 bit only, on a 32 bit architecture this
means factor 32 less RAM and ~ factor 32 more speed on boolean operations.
Due to overhead of R calls, actual speed gain depends on the size of the
vector: expect gains for vectors of size > 10000 elements. Even for
one-time boolean operations it can pay-off to convert to bit, the pay-off
is obvious, when such components are used more than once. Reading from and
writing to bit is approximately as fast as accessing standard logicals -
mostly due to R's time for memory allocation. The package allows to work
with pre-allocated memory for return values by calling .Call() directly:
when evaluating the speed of C-access with pre-allocated vector memory,
coping from bit to logical requires only 70% of the time for copying from
logical to logical; and copying from logical to bit comes at a performance
penalty of 150%. the package now contains further classes for representing
logical selections: 'bitwhich' for very skewed selections and 'ri' for
selecting ranges of values for chunked processing. All three index classes
can be used for subsetting 'ff' objects (ff-2.1-0 and higher).

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
%doc %{rlibdir}/%{packname}/exec
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ANNOUNCEMENT-1.0.txt
%doc %{rlibdir}/%{packname}/README_devel.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
