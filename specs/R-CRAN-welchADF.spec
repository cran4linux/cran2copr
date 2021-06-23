%global __brp_check_rpaths %{nil}
%global packname  welchADF
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Welch-James Statistic for Robust Hypothesis Testing underHeterocedasticity and Non-Normality

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-lme4 

%description
Implementation of Johansen's general formulation of Welch-James's
statistic with Approximate Degrees of Freedom, which makes it suitable for
testing any linear hypothesis concerning cell means in univariate and
multivariate mixed model designs when the data pose non-normality and
non-homogeneous variance. Some improvements, namely trimmed means and
Winsorized variances, and bootstrapping for calculating an empirical
critical value, have been added to the classical formulation. The code
departs from a previous SAS implementation by L.M. Lix and H.J. Keselman,
available at
<http://supp.apa.org/psycarticles/supplemental/met_13_2_110/SAS_Program.pdf>
and published in Keselman, H.J., Wilcox, R.R., and Lix, L.M. (2003)
<DOI:10.1111/1469-8986.00060>.

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
