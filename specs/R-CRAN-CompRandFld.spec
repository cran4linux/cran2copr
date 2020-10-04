%global packname  CompRandFld
%global packver   1.0.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3.6
Release:          3%{?dist}%{?buildtag}
Summary:          Composite-Likelihood Based Analysis of Random Fields

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-mapproj 
Requires:         R-methods 
Requires:         R-CRAN-maps 

%description
A set of procedures for the analysis of Random Fields using likelihood and
non-standard likelihood methods is provided. Spatial analysis often
involves dealing with large dataset. Therefore even simple studies may be
too computationally demanding. Composite likelihood inference is emerging
as a useful tool for mitigating such computational problems. This
methodology shows satisfactory results when compared with other techniques
such as the tapering method. Moreover, composite likelihood (and related
quantities) have some useful properties similar to those of the standard
likelihood. Adapts the methodologies derived in Padoan and Bevilacqua
(2015) <doi:10.18637/jss.v063.i09>, Padoan et al. (2010)
<doi:10.1198/jasa.2009.tm08577>, Davison et al. (2012)
<doi:10.1214/11-STS376>, Bevilacqua et al. (2012)
<doi:10.1080/01621459.2011.646928>. It also refers to the works of
Bevilacqua et al. (2010) <doi:10.1007/s11222-009-9121-3>, Bevilacqua and
Gaetan (2013) <doi:10.1007/s11222-014-9460-6>, Cooley et al. (2006)
<doi:10.1007/0-387-36062-X_17>, Cressie (1993)
<doi:10.1002/9781119115151>, Gaetan and Guyon (2010)
<doi:10.1007/978-0-387-92257-7>, Gneiting (2002)
<doi:10.1198/016214502760047113>, Gneiting et al. (2007)
<https://www.stat.washington.edu/sites/default/files/files/reports/2005/tr475.pdf>,
Heagerty and Zeger (1998) <doi:10.1080/01621459.1998.10474097>, Harville
(1977) <doi:10.2307/2286796>, Kaufman et al. (2008)
<doi:10.1198/016214508000000959>, Shaby and Ruppert (2012)
<doi:10.1080/10618600.2012.680819>, Varin and Vidoni (2005)
<doi:10.1093/biomet/92.3.519>, Patrick et al.
<doi:10.1080/01621459.1998.10473771>, de Haan and Pereira (2006)
<doi:10.1214/009053605000000886>, Kabluchko (2010)
<doi:10.1007/s10687-010-0110-x>, Kabluchko et al. (2009)
<doi:10.1214/09-AOP455>, Schlather (2002) <doi:10.1023/A:1020977924878>,
Carlstein (1986) <doi:10.1214/aos/1176350057>, Heagerty and Lumley (2000)
<doi:10.2307/2669538>, Lee and Lahiri (2002)
<doi:10.1111/1467-9868.00364>, Li et al. (2007)
<doi:10.1198/016214507000000202>, de Haan and Ferreira (2006)
<doi:10.1007/0-387-34471-3> Smith (1987) <doi:10.1093/biomet/72.1.67>,
Chandler and Bate (2007) <doi:10.1093/biomet/asm015>, Rotnitzky and Jewell
(1990) <doi:10.1093/biomet/77.3.485>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
