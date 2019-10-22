%global packname  tempoR
%global packver   1.0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4.4
Release:          1%{?dist}
Summary:          Characterizing Temporal Dysregulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.0.2
BuildRequires:    R-CRAN-pls >= 2.5.0
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-parallel >= 3.0.2
Requires:         R-CRAN-pls >= 2.5.0
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
TEMPO (TEmporal Modeling of Pathway Outliers) is a pathway-based outlier
detection approach for finding pathways showing significant changes in
temporal expression patterns across conditions.  Given a gene expression
data set where each sample is characterized by an age or time point as
well as a phenotype (e.g. control or disease), and a collection of gene
sets or pathways, TEMPO ranks each pathway by a score that characterizes
how well a partial least squares regression (PLSR) model can predict age
as a function of gene expression in the controls and how poorly that same
model performs in the disease. TEMPO v1.0.3 is described in Pietras (2018)
<doi:10.1145/3233547.3233559>.

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
%doc %{rlibdir}/%{packname}/dflatExample.gmt
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gse32472Example.age.cls
%doc %{rlibdir}/%{packname}/gse32472Example.gct
%doc %{rlibdir}/%{packname}/gse32472Example.phen.cls
%{rlibdir}/%{packname}/INDEX
