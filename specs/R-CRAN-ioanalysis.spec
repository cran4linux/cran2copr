%global packname  ioanalysis
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Input Output Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plot3D 

%description
Calculates fundamental IO matrices (Leontief, Wassily W. (1951)
<doi:10.1038/scientificamerican1051-15>); within period analysis via
various rankings and coefficients (Sonis and Hewings (2006)
<doi:10.1080/09535319200000013>, Blair and Miller (2009)
<ISBN:978-0-521-73902-3>, Antras et al (2012) <doi:10.3386/w17819>,
Hummels, Ishii, and Yi (2001) <doi:10.1016/S0022-1996(00)00093-3>); across
period analysis with impact analysis (Dietzenbacher, van der Linden, and
Steenge (2006) <doi:10.1080/09535319300000017>, Sonis, Hewings, and Guo
(2006) <doi:10.1080/09535319600000002>); and a variety of table operators.

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
%{rlibdir}/%{packname}/INDEX
