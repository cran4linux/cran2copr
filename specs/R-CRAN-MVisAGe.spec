%global packname  MVisAGe
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Compute and Visualize Bivariate Associations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch

%description
Pearson and Spearman correlation coefficients are commonly used to
quantify the strength of bivariate associations of genomic variables.  For
example, correlations of gene-level DNA copy number and gene expression
measurements may be used to assess the impact of DNA copy number changes
on gene expression in tumor tissue.  'MVisAGe' enables users to quickly
compute and visualize the correlations in order to assess the effect of
regional genomic events such as changes in DNA copy number or DNA
methylation level.  Please see Walter V, Du Y, Danilova L, Hayward MC,
Hayes DN, 2018. Cancer Research <doi:10.1158/0008-5472.CAN-17-3464>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
