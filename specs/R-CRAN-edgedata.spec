%global packname  edgedata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Datasets that Support the EDGE Server DIY Logic

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch

%description
Datasets from (Excel download)
<https://www.cms.gov/CCIIO/Resources/Regulations-and-Guidance/Downloads/CY2019-DIY-tables.01.17.20.xlsx>
and (ZIP download)
<https://www.cms.gov/CCIIO/Resources/Regulations-and-Guidance/Downloads/HHS-HCC-2019-software.01.17.2020.zip>
in a tidy format. These support the Centers for Medicare and Medicaid
Services' (CMS) risk adjustment Do-It-Yourself (DIY) process, which allows
health insurance issuers to calculate member risk profiles under the
Health and Human Services-Hierarchical Condition Categories (HHS-HCC)
regression model. This regression model is used to calculate risk
adjustment transfers. Risk adjustment is a selection mitigation program
implemented under the Patient Protection and Affordable Care Act (ACA or
Obamacare) in the USA. Under the ACA, health insurance issuers submit
claims data to CMS in order for CMS to calculate a risk score under the
HHS-HCC regression model. However, CMS does not inform issuers of their
average risk score until after the data submission deadline. These data
sets can be used by issuers to calculate their average risk score
mid-year. More information about risk adjustment and the HHS-HCC model can
be found here:
<https://www.cms.gov/mmrr/Articles/A2014/MMRR2014_004_03_a03.html>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
