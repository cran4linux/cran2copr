%global __brp_check_rpaths %{nil}
%global packname  KenSyn
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Knowledge Synthesis in Agriculture - From Experimental Networkto Meta-Analysis

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-metafor 
Requires:         R-nlme 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-metafor 

%description
Demo and dataset accompaying the books : De l'analyse des réseaux
expérimentaux à la méta-analyse: Méthodes et applications avec le logiciel
R pour les sciences agronomiques et environnementales (Published
2018-06-28, Quae, for french version) by David Makowski, Francois Piraux
and Francois Brun -
<https://www.quae.com/produit/1514/9782759228164/de-l-analyse-des-reseaux-experimentaux-a-la-meta-analyse>
Knowledge Synthesis in Agriculture : from Experimental Network to
Meta-Analysis (in preparation for 2018-06, Springer , for English version)
by David Makowski, Francois Piraux and Francois Brun A full description of
all the material is in both books. ACKNOWLEDGMENTS : The French network
"RMT modeling and data analysis for agriculture"
(<http://www.modelia.org>) have contributed to the development of this R
package. This project and network are lead by ACTA (French Technical
Institute for Agriculture) and was funded by a grant from the Ministry of
Agriculture and Fishing of France.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
