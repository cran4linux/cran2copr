%global packname  doex
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          The One-Way Heteroscedastic ANOVA Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Contains several one-way heteroscedastic ANOVA tests such as
Alexander-Govern test by Alexandern and Govern (1994)
<doi:10.2307/1165140>, Alvandi et al. Generalized F test by Alvandi et al.
(2012) <doi:10.1080/03610926.2011.573160>, Approximate F test by Asiribo
and Gurland (1990) <doi:10.1080/03610929008830427>, Box F test by Box
(1954) <doi:10.1214/aoms/1177728786>, Brown-Forsythe test by Brown and
Forsythe (1974) <do:10.2307/1267501>, B2 test by Ozdemir and Kurt (2006)
<http://sjam.selcuk.edu.tr/sjam/article/view/174>, Cochran F test by
Cochran (1937) <https://www.jstor.org/stable/pdf/2984123.pdf>, Fiducial
Approach test by Li et al. (2011) <doi:10.1016/j.csda.2010.12.009>,
Generalized F test by Weerahandi (1995) <doi:10.2307/2532947>, Johansen F
test by Johansen (1980) <doi:10.1093/biomet/67.1.85>, Modified
Brown-Forsythe test by Mehrotra (1997) <doi:10.1080/03610919708813431>,
Modified Welch test by Hartung et al.(2002)
<doi:10.1007/s00362-002-0097-8>, One-Stage test by Chen and Chen (1998)
<doi:10.1080/03610919808813501>, One-Stage Range test by Chen and Chen
(2000) <doi:10.1080/01966324.2000.10737505>, Parametric Bootstrap test by
Krishnamoorhty et al.(2007) <doi:10.1016/j.csda.2006.09.039>, Permutation
F test by Berry and Mielke (2002) <doi:10.2466/pr0.2002.90.2.495>,
Scott-Smith test by Scott and Smith (1971) <doi:10.2307/2346757>, Welch
test by Welch(1951) <doi:10.2307/2332579>, and Welch-Aspin test by Aspin
(1948) <doi:10.1093/biomet/35.1-2.88>. These tests are used to test the
equality of group means under unequal variance. Furthermore, a modified
version of Generalized F-test is improved to test the equality of
non-normal group means under unequal variances and a revised version of
Generalized F-test is given to test the equality of non-normal group means
caused by skewness.

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
