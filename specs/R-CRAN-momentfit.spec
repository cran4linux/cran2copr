%global packname  momentfit
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Methods of Moments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-parallel 

%description
Several classes for moment-based models are defined. The classes are
defined for moment conditions derived from a single equation or a system
of equations. The conditions can also be expressed as functions or
formulas. Several methods are also offered to facilitate the development
of different estimation techniques. The methods that are currently
provided are the Generalized method of moments (Hansen 1982;
<doi:10.2307/1912775>), for single equations and systems of equation, and
the Generalized Empirical Likelihood (Smith 1997;
<doi:10.1111/j.0013-0133.1997.174.x>, Kitamura 1997;
<doi:10.1214/aos/1069362388>, Newey and Smith 2004;
<doi:10.1111/j.1468-0262.2004.00482.x>, and Anatolyev 2005
<doi:10.1111/j.1468-0262.2005.00601.x>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
