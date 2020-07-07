%global packname  praznik
%global packver   8.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.0.0
Release:          3%{?dist}
Summary:          Tools for Information-Based Feature Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
A toolbox of fast, native and parallel implementations of various
information-based importance criteria estimators and feature selection
filters based on them, inspired by the overview by Brown, Pocock, Zhao and
Lujan (2012) <http://www.jmlr.org/papers/v13/brown12a.html>. Contains,
among other, minimum redundancy maximal relevancy ('mRMR') method by Peng,
Long and Ding (2005) <doi:10.1109/TPAMI.2005.159>; joint mutual
information ('JMI') method by Yang and Moody (1999)
<http://papers.nips.cc/paper/1779-data-visualization-and-feature-selection-new-algorithms-for-nongaussian-data>;
double input symmetrical relevance ('DISR') method by Meyer and Bontempi
(2006) <doi:10.1007/11732242_9> as well as joint mutual information
maximisation ('JMIM') method by Bennasar, Hicks and Setchi (2015)
<doi:10.1016/j.eswa.2015.07.007>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
