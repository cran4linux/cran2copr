%global packname  additiveDEA
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Additive Data Envelopment Analysis Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-Benchmarking 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-Benchmarking 

%description
Provides functions for calculating efficiency with two types of additive
Data Envelopment Analysis models: (i) Generalized Efficiency Measures:
unweighted additive model (Cooper et al., 2007
<doi:10.1007/978-0-387-45283-8>), Range Adjusted Measure (Cooper et al.,
1999, <doi:10.1023/A:1007701304281>), Bounded Adjusted Measure (Cooper et
al., 2011 <doi:10.1007/s11123-010-0190-2>), Measure of Inefficiency
Proportions (Cooper et al., 1999 <doi:10.1023/A:1007701304281>), and the
Lovell-Pastor Measure (Lovell and Pastor, 1995
<doi:10.1016/0167-6377(95)00044-5>); and (ii) the Slacks-Based Measure
(Tone, 2001 <doi:10.1016/S0377-2217(99)00407-5>). The functions provide
several options: (i) constant and variable returns to scale; (ii) fixed
(non-controllable) inputs and/or outputs; (iii) bounding the slacks so
that unrealistically large slack values are avoided; and (iv) calculating
the efficiency of specific Decision-Making Units (DMUs), rather than of
the whole sample. Package additiveDEA also provides a function for
reducing computation time when datasets are large.

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
