%global packname  ChillModels
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Processing Chill and Heat Models for Temperate Fruit Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch

%description
Calculates the chilling and heat accumulation for studies of the temperate
fruit trees. The models in this package are: Utah (Richardson et al.,
1974, ISSN:0018-5345), Positive Chill Units - PCU (Linsley-Noaks et al.,
1995, ISSN:1017-0316), GDH-A - Growing Degree Hours by Anderson et
al.(1986, ISSN:0567-7572), GDH-R - Growing Degree Hours by Richardson et
al.(1975, ISSN:0018-5345), North Carolina (Shaltout e Unrath, 1983,
ISSN:0003-1062), Landsberg Model (Landsberg, 1974, ISSN:0305-7364), Q10
Model (Bidabe, 1967, ISSN:0031-9368), Jones Model (Jones et al., 2013
<DOI:10.1111/j.1438-8677.2012.00590.x>), Low-Chill Model (Gilreath and
Buchanan, 1981, ISSN:0003-1062), Model for Cherry "Sweetheart" (Guak and
Nielsen, 2013 <DOI:10.1007/s13580-013-0140-9>), Model for apple "Gala"
(Guak and Nielsen, 2013 <DOI:10.1007/s13580-013-0140-9>), Taiwan Model (Lu
et al., 2012 <DOI:10.17660/ActaHortic.2012.962.35>), Dynamic Model
(Fishman et al., 1987, ISSN:0022-5193) adapted from the function
Dynamic_Model() of the 'chillR' package (Luedeling, 2018), Unified Model
(Chuine et al., 2016 <DOI:10.1111/gcb.13383>) and Heat Restriction model.

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
%{rlibdir}/%{packname}/INDEX
