%global packname  electoral
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Allocating Seats Methods and Party System Scores

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-tibble 

%description
Highest averages & largest remainders allocating seats methods and several
party system scores. Implemented highest averages allocating seats methods
are D'Hondt, Webster, Danish, Imperiali, Hill-Huntington, Dean, Modified
Sainte-Lague, equal proportions and Adams. Implemented largest remainders
allocating seats methods are Hare, Droop, Hangenbach-Bischoff, Imperial,
modified Imperial and quotas & remainders. The main advantage of this
package is that ties are always reported and not incorrectly allocated.
Party system scores provided are competitiveness, concentration, effective
number of parties, party nationalization score, party system
nationalization score and volatility. References: Gallagher (1991)
<doi:10.1016/0261-3794(91)90004-C>. Norris (2004, ISBN:0-521-82977-1).
Consejo Nacional Electoral del Ecuador
(2014)<http://cne.gob.ec/documents/Estadisticas/Atlas/ATLAS/CAPITULO%206%20web.pdf>.
Laakso & Taagepera (1979)
<http://journals.sagepub.com/doi/pdf/10.1177/001041407901200101>. Jones &
Mainwaring (2003)
<https://kellogg.nd.edu/sites/default/files/old_files/documents/304_0.pdf>.
Pedersen (1979) <http://janda.org/c24/Readings/Pedersen/Pedersen.htm>.
Golosov (2010) <http://ppq.sagepub.com/content/16/2/171.abstract>. Golosov
(2014)
<http://ppq.sagepub.com/content/early/2014/09/08/1354068814549342.abstract>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
