%global packname  ulid
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Generate Universally Unique Lexicographically SortableIdentifiers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Universally unique identifiers ('UUIDs') can be suboptimal for many
uses-cases because they aren't the most character efficient way of
encoding 128 bits of randomness; v1/v2 versions are impractical in many
environments, as they require access to a unique, stable MAC address;
v3/v5 versions require a unique seed and produce randomly distributed IDs,
which can cause fragmentation in many data structures; v4 provides no
other information than randomness which can cause fragmentation in many
data structures. 'ULIDs' (<https://github.com/ulid/spec>) have 128-bit
compatibility with 'UUID', 1.21e+24 unique 'ULIDs' per millisecond, are
lexicographically sortable, canonically encoded as a 26 character string,
as opposed to the 36 character 'UUID', use Crockford's 'base32' for better
efficiency and readability (5 bits per character), are case insensitive,
have no special characters (i.e. are 'URL' safe) and have a onotonic sort
order (correctly detects and handles the same millisecond).

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
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
