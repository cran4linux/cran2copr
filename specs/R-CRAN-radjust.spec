%global packname  radjust
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Replicability Adjusted p-Values for Two Independent Studies withMultiple Endpoints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Calculates adjusted p-values for the null hypothesis of no replicability
across studies for two study designs: (i) a primary and follow-up study,
where the features in the follow-up study are selected from the primary
study, as described in Bogomolov and Heller (2013)
<doi:10.1080/01621459.2013.829002> and Heller, Bogomolov and Benjamini
(2014) <doi:10.1073/pnas.1314814111>; (ii) two independent studies, where
the features for replicability are first selected in each study
separately, as described in Bogomolov and Heller (2018)
<doi:10.1093/biomet/asy029>. The latter design is the one encountered in a
typical meta-analysis of two studies, but the inference is for
replicability rather than for identifying the features that are non-null
in at least one study.

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
%{rlibdir}/%{packname}/INDEX
